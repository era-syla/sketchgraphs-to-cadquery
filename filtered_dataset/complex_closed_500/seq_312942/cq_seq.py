import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00285, -0.05077).lineTo(0.00285, -0.05077).lineTo(0.00285, -0.05636).lineTo(-0.00285, -0.05636).lineTo(-0.00285, -0.05077).close()
solid=wp_sketch0.add(loop0).extrude(-0.013211519136908746)
