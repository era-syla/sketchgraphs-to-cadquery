import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.048, 0.0325).lineTo(-0.008, 0.0325).lineTo(-0.008, 0.0675).lineTo(-0.048, 0.0675).lineTo(-0.048, 0.0325).close()
solid=wp_sketch0.add(loop0).extrude(-0.10729836166383364)
