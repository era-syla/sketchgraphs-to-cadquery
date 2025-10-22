import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0365, 0.06501).lineTo(0.0815, 0.06501).lineTo(0.0815, 0.06701).lineTo(0.0365, 0.06701).lineTo(0.0365, 0.06501).close()
solid=wp_sketch0.add(loop0).extrude(-0.10758323059269571)
