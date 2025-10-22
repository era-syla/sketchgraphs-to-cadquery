import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00273, -0.00173).lineTo(-0.02301, -0.00173).lineTo(-0.02301, -0.00693).lineTo(0.00273, -0.00693).lineTo(0.00273, -0.00173).close()
solid=wp_sketch0.add(loop0).extrude(-0.0759340533255595)
