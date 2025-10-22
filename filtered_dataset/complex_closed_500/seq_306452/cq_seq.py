import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.008, 0.03825).lineTo(0.008, 0.03825).lineTo(0.008, 0.02962).lineTo(-0.008, 0.02962).lineTo(-0.008, 0.03825).close()
solid=wp_sketch0.add(loop0).extrude(0.0021758845824389255)
