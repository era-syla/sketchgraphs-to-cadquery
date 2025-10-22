import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 1.04993).lineTo(0.05, 1.04993).lineTo(0.05, -1.05007).lineTo(0.0, -1.05007).lineTo(0.0, 1.04993).close()
solid=wp_sketch0.add(loop0).extrude(-4.148627098359796)
