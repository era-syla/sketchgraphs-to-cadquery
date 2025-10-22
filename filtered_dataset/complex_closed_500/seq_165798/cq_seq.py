import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0153, 0.0021).lineTo(-0.0178, 0.0021).lineTo(-0.0178, 0.0063).lineTo(-0.0153, 0.0063).lineTo(-0.0153, 0.0021).close()
solid=wp_sketch0.add(loop0).extrude(0.006467156351246896)
