import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(-5.8, 0.0).lineTo(-5.8, -0.5).threePointArc((-2.9, -0.217), (0.0, -0.5)).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(12.14755271232272)
