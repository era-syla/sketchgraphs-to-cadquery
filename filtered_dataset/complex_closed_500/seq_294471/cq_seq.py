import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.02425, -0.001).lineTo(-0.02125, -0.001).lineTo(-0.02125, -0.013).lineTo(0.02125, -0.013).lineTo(0.02125, -0.001).lineTo(0.02425, -0.001).lineTo(0.02425, -0.016).lineTo(-0.02425, -0.016).lineTo(-0.02425, -0.001).close()
solid=wp_sketch0.add(loop0).extrude(0.0867892030126567)
