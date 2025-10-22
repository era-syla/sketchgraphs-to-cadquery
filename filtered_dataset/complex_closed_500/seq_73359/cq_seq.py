import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.023, -0.005).lineTo(0.051, -0.005).lineTo(0.051, -0.015).lineTo(0.056, -0.015).lineTo(0.056, 0.01).lineTo(0.051, 0.01).lineTo(0.051, 0.0).lineTo(0.023, 0.0).lineTo(0.023, -0.005).close()
solid=wp_sketch0.add(loop0).extrude(0.01616843755973813)
