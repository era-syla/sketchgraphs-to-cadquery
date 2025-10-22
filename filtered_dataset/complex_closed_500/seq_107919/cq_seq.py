import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.89, -7.44842).lineTo(7.8413, -7.44842).lineTo(7.8413, 6.67101).lineTo(-0.89, 6.67101).lineTo(-0.89, -7.44842).close()
solid=wp_sketch0.add(loop0).extrude(7.139450839680538)
