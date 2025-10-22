import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.27837, 0.38286).lineTo(0.22963, 0.38286).lineTo(0.22963, -0.37914).lineTo(-0.27837, -0.37914).lineTo(-0.27837, 0.38286).close()
solid=wp_sketch0.add(loop0).extrude(-1.1733251202670871)
