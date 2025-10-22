import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(1.47063, 0.98331).lineTo(0.07063, 0.98331).lineTo(0.07063, 0.38331).lineTo(1.47063, 0.38331).lineTo(1.47063, 0.98331).close()
solid=wp_sketch0.add(loop0).extrude(1.0993487682150915)
