import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.26653, -0.38732).lineTo(0.40791, -0.38732).lineTo(0.40791, -0.45817).lineTo(-0.26653, -0.45817).lineTo(-0.26653, -0.38732).close()
solid=wp_sketch0.add(loop0).extrude(-1.1349883597789243)
