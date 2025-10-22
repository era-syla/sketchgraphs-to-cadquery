import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.008, 0.007).lineTo(-0.008, 0.0056).lineTo(0.008, 0.0056).lineTo(0.008, 0.007).lineTo(-0.008, 0.007).close()
solid=wp_sketch0.add(loop0).extrude(-0.03942192050410513)
