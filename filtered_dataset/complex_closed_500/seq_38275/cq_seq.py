import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.41109, -0.02359).lineTo(-0.41117, -0.15126).lineTo(-0.41552, -0.15145).lineTo(-0.41387, -0.02358).lineTo(-0.41109, -0.02359).close()
solid=wp_sketch0.add(loop0).extrude(-0.1541529476038035)
