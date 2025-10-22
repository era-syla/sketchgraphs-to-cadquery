import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.07144, 0.61119).lineTo(0.30004, 0.61119).lineTo(0.30004, 0.48419).lineTo(0.07144, 0.48419).lineTo(0.07144, 0.61119).close()
solid=wp_sketch0.add(loop0).extrude(0.040289033083015756)
