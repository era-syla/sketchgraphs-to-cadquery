import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.2032, 0.2032).lineTo(-0.2032, 0.2032).lineTo(-0.2032, -0.2032).lineTo(0.2032, -0.2032).lineTo(0.2032, 0.2032).close()
solid=wp_sketch0.add(loop0).extrude(-0.01017995315844149)
