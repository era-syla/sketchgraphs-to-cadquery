import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.11741, -0.12456).lineTo(-0.35931, -0.12456).lineTo(-0.35931, -0.53096).lineTo(-0.11741, -0.53096).lineTo(-0.11741, -0.12456).close()
solid=wp_sketch0.add(loop0).extrude(1.0800535123486694)
