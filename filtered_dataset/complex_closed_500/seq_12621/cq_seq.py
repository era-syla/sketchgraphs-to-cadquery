import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0197, 0.01232).lineTo(-0.0347, 0.01232).lineTo(-0.0347, 0.00332).lineTo(-0.0197, 0.00332).lineTo(-0.0197, 0.01232).close()
solid=wp_sketch0.add(loop0).extrude(0.043499093320374965)
