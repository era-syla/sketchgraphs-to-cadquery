import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.04801, 0.05414).lineTo(-0.0636, 0.05414).lineTo(-0.0636, 0.07113).lineTo(-0.04801, 0.07113).lineTo(-0.04801, 0.05414).close()
solid=wp_sketch0.add(loop0).extrude(-0.0485421474223528)
