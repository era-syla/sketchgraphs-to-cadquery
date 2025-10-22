import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.06075, 0.00639).lineTo(0.13547, 0.00639).lineTo(0.13547, -0.06482).lineTo(-0.06075, -0.06482).lineTo(-0.06075, 0.00639).close()
solid=wp_sketch0.add(loop0).extrude(0.24078619728588638)
