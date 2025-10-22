import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.04098, 0.08809).lineTo(-0.01559, 0.0999).lineTo(-0.01391, 0.09627).lineTo(-0.01947, 0.08927).lineTo(-0.03761, 0.08083).lineTo(-0.04098, 0.08809).close()
solid=wp_sketch0.add(loop0).extrude(-0.012710773592610372)
