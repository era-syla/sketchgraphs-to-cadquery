import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.4699, 0.0).lineTo(-0.0127, 0.0).lineTo(-0.0127, 0.05715).lineTo(-0.4699, 0.05715).lineTo(-0.4699, -0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.05066950815013646)
