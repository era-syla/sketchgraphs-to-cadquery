import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.001, 0.0).lineTo(-0.002, 0.001).lineTo(-0.0, 0.001).lineTo(0.0, 0.0).lineTo(-0.001, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.0026520352124725444)
