import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.1397, 4.51803).lineTo(0.0, 4.51803).lineTo(0.0, 6.34683).lineTo(-0.1397, 6.34683).lineTo(-0.1397, 4.51803).close()
solid=wp_sketch0.add(loop0).extrude(5.032259763972339)
