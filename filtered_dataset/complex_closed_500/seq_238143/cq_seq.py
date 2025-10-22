import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.07182, -0.07354).lineTo(0.07083, -0.07354).lineTo(0.07083, 0.05408).lineTo(-0.07182, 0.05408).lineTo(-0.07182, -0.07354).close()
solid=wp_sketch0.add(loop0).extrude(0.2473549740708892)
