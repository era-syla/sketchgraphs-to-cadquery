import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.022, 0.009).lineTo(-0.012, 0.009).lineTo(-0.012, -0.003).lineTo(-0.022, -0.003).lineTo(-0.022, 0.009).close()
solid=wp_sketch0.add(loop0).extrude(0.017378227520996357)
