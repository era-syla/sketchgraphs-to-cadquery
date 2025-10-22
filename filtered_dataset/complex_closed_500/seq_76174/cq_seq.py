import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.06499, -0.14001).lineTo(-0.02999, -0.14001).threePointArc((-0.04024, -0.11526), (-0.06499, -0.10501)).lineTo(-0.06499, -0.14001).close()
solid=wp_sketch0.add(loop0).extrude(-0.06910446902084535)
