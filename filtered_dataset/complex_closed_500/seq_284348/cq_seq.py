import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-9.47336, -5.75834).lineTo(8.50422, -5.75834).lineTo(8.50422, 11.55551).lineTo(-9.47336, 11.55551).lineTo(-9.47336, -5.75834).close()
solid=wp_sketch0.add(loop0).extrude(-33.6887319412798)
