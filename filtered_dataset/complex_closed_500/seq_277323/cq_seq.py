import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.4826, 0.38735).lineTo(-0.3302, 0.38735).lineTo(-0.3302, 0.2286).lineTo(-0.4826, 0.2286).lineTo(-0.4826, 0.38735).close()
solid=wp_sketch0.add(loop0).extrude(0.13396789314465452)
