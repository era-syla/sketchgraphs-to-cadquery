import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0125, 0.0175).lineTo(0.0125, 0.0175).lineTo(0.00811, 0.03509).lineTo(-0.00811, 0.03509).lineTo(-0.0125, 0.0175).close()
solid=wp_sketch0.add(loop0).extrude(0.054330233120401285)
