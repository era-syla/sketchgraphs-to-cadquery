import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.184, 0.001).lineTo(-0.09, 0.001).lineTo(-0.09, 0.046).lineTo(-0.184, 0.046).lineTo(-0.184, 0.001).close()
solid=wp_sketch0.add(loop0).extrude(0.1925335026753678)
