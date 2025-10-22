import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.01018, 0.01476).lineTo(-0.00518, 0.01476).lineTo(-0.00518, 0.00976).lineTo(-0.01018, 0.00976).lineTo(-0.01018, 0.01476).close()
solid=wp_sketch0.add(loop0).extrude(0.003934255535288743)
