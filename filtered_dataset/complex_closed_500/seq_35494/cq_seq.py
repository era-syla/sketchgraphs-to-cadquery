import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.01275, -0.0017).lineTo(0.01275, -0.0017).lineTo(0.01275, -0.0065).lineTo(-0.01275, -0.0065).lineTo(-0.01275, -0.0017).close()
solid=wp_sketch0.add(loop0).extrude(-0.021454141625889937)
