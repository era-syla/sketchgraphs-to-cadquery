import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.06376, 0.05674).lineTo(-0.05176, 0.05674).lineTo(-0.05176, -0.04626).lineTo(-0.06376, -0.04626).lineTo(-0.06376, 0.05674).close()
solid=wp_sketch0.add(loop0).extrude(0.14568294261230558)
