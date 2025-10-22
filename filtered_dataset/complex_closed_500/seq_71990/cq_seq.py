import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.09582, 0.05413).lineTo(-0.07216, 0.05413).lineTo(-0.07216, 0.03825).lineTo(-0.09582, 0.03825).lineTo(-0.09582, 0.05413).close()
solid=wp_sketch0.add(loop0).extrude(0.03946842989705454)
