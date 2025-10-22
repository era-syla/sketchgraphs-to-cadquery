import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00479, -0.00509).lineTo(0.00168, 0.00772).lineTo(-0.00647, -0.00265).lineTo(-0.00144, -0.00661).lineTo(0.00479, -0.00509).close()
solid=wp_sketch0.add(loop0).extrude(0.02301989402666214)
