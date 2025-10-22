import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.20386, 0.58472).lineTo(-0.22926, 0.58472).lineTo(-0.22932, 0.57408).lineTo(-0.20386, 0.58472).close()
solid=wp_sketch0.add(loop0).extrude(-0.04582393869165057)
