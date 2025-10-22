import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.05073, 0.02958).lineTo(-0.00769, 0.02958).lineTo(-0.00769, 0.01845).lineTo(-0.05073, 0.01845).lineTo(-0.05073, 0.02958).close()
solid=wp_sketch0.add(loop0).extrude(0.02991691139254996)
