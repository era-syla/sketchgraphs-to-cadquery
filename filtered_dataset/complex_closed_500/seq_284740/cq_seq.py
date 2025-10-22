import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.036, 0.0).lineTo(-0.036, 0.0).lineTo(-0.036, 0.0508).lineTo(0.036, 0.0508).lineTo(0.036, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.07907327920509268)
