import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0381, 0.4191).lineTo(3.048, 0.4191).lineTo(3.048, 1.1049).lineTo(0.0381, 1.1049).lineTo(0.0381, 0.4191).close()
solid=wp_sketch0.add(loop0).extrude(8.159069378896726)
