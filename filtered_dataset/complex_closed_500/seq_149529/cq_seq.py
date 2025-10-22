import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.05483, 0.0).lineTo(-0.02383, 0.0).lineTo(-0.02383, -0.0149).lineTo(-0.05483, -0.0149).lineTo(-0.05483, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.005083628115989673)
