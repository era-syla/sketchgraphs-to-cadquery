import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.035, 0.0032).lineTo(0.0472, -0.009).lineTo(0.03801, -0.009).lineTo(0.0304, -0.0014).lineTo(0.035, 0.0032).close()
solid=wp_sketch0.add(loop0).extrude(0.029017236468391345)
