import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.05622, 0.0597).lineTo(0.07122, 0.0597).lineTo(0.07122, 0.0747).lineTo(0.05622, 0.0747).lineTo(0.05622, 0.0597).close()
solid=wp_sketch0.add(loop0).extrude(-0.010557115239670694)
