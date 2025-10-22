import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.01954, 0.02928).lineTo(-0.01954, 0.02822).lineTo(-0.02211, 0.03188).lineTo(-0.02173, 0.03215).lineTo(-0.01954, 0.02928).close()
solid=wp_sketch0.add(loop0).extrude(-0.001109240482961147)
