import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0, -0.1016).lineTo(0.12725, -0.1016).threePointArc((0.20912, -0.06795), (0.28482, -0.02206)).lineTo(0.25297, 0.0).lineTo(0.2032, 0.0).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.19415047823388773)
