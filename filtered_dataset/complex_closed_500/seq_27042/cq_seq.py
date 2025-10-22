import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.26617, -0.25443).lineTo(0.32322, -0.25443).lineTo(0.32322, 0.26644).lineTo(-0.26617, 0.26644).lineTo(-0.26617, -0.25443).close()
solid=wp_sketch0.add(loop0).extrude(-0.9330540487848484)
