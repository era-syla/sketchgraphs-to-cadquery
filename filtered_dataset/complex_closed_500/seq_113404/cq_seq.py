import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.06683, 0.02588).lineTo(0.07335, 0.02588).lineTo(0.07335, -0.02686).lineTo(-0.06683, -0.02686).lineTo(-0.06683, 0.02588).close()
solid=wp_sketch0.add(loop0).extrude(-0.3741140340717715)
