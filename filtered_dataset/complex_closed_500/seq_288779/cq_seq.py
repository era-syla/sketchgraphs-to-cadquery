import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00625, 0.0).lineTo(0.00625, 0.0).lineTo(0.0037, 0.00255).lineTo(0.0022, 0.00255).lineTo(0.0022, 0.00355).lineTo(0.0016, 0.00355).lineTo(0.0016, 0.00255).lineTo(-0.0016, 0.00255).lineTo(-0.0016, 0.00355).lineTo(-0.0022, 0.00355).lineTo(-0.0022, 0.00255).lineTo(-0.0037, 0.00255).lineTo(-0.00625, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.003419213766237744)
