import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00244, 0.004).lineTo(0.02156, 0.004).lineTo(0.02825, 0.016).lineTo(0.03225, 0.016).lineTo(0.024, 0.0).lineTo(-0.0, -0.0).lineTo(-0.00687, 0.01333).lineTo(-0.00287, 0.01333).lineTo(0.00244, 0.004).close()
solid=wp_sketch0.add(loop0).extrude(0.004251275904433096)
