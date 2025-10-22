import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0905, 0.0137).threePointArc((-0.0855, 0.0087), (-0.0805, 0.0137)).lineTo(-0.0905, 0.0137).close()
solid=wp_sketch0.add(loop0).extrude(-0.027780717374864768)
