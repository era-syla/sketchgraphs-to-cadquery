import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00513, 0.20769).lineTo(-0.00811, 0.20769).lineTo(-0.00811, 0.18264).lineTo(0.00513, 0.18264).lineTo(0.00513, 0.20769).close()
solid=wp_sketch0.add(loop0).extrude(0.06701217736831357)
