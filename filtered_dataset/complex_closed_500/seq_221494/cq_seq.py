import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0, 0.08).lineTo(-0.005, 0.08).lineTo(-0.005, 0.004).lineTo(-0.02, 0.004).lineTo(-0.02, -0.0).lineTo(-0.025, -0.0).lineTo(-0.025, -0.005).lineTo(0.0, -0.005).lineTo(0.0, 0.0).lineTo(-0.0, 0.08).close()
solid=wp_sketch0.add(loop0).extrude(0.04882644822413154)
