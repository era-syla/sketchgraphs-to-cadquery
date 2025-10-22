import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.37, 0.0).lineTo(0.37, 1.2073).lineTo(-0.0, 1.2073).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.4333487415763908)
